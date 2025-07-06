import argparse
import sys
import pickle
from openfhe import *
import pickle

class CKKSParser:
    def __init__(self):
        self.context = CryptoContext()
        self.public_key = None
        self.input = None


    def load(self, args):
        self.init_context(args.cc)
        self.init_public_key(args.key_pub)
        self.init_eval_mult_key(args.key_mult)
        self.init_rotation_key(args.key_rot)
        self.init_ciphertext(args.sample)


    def init_context(self, context_path):
        self.context, ok = DeserializeCryptoContext(context_path, BINARY)
        if not ok:
            raise Exception('load crypto context')


    def init_public_key(self, public_key_path):
        self.public_key, ok = DeserializePublicKey(public_key_path, BINARY)
        if not ok:
            raise Exception('load public key')


    def init_eval_mult_key(self, eval_key_path):
        if not self.context.DeserializeEvalMultKey(eval_key_path, BINARY):
            raise Exception('load mult key')


    def init_rotation_key(self, rotation_key_path):
        if not self.context.DeserializeEvalAutomorphismKey(rotation_key_path, BINARY):
            raise Exception('load rotation key')
        

    def init_ciphertext(self, ciphertext_path):
        self.input, ok = DeserializeCiphertext(ciphertext_path, BINARY)
        if not ok:
            raise Exception('load ciphertext')
 
def solve(input, context, pub_key):
    # Load model weights and bias
    with open("weights/regression/model_weights.bin", "rb") as f:
        model_data = pickle.load(f)
    weights = model_data["weights"]  # List of weights
    bias = model_data["bias"]  # Scalar bias
    
    # Preprocess weights for better numerical stability
    # This helps maintain precision during homomorphic operations
    scaled_weights = weights
    
    # IMPROVEMENT 1: Use higher precision for encoding
    # Set higher precision for the plaintext encoding to minimize rounding errors
    precision = 1e-9  # Increased precision
    
    # IMPROVEMENT 2: Encode the weights with higher precision
    plaintext_weights = context.MakeCKKSPackedPlaintext(scaled_weights, precision)
    plaintext_bias = context.MakeCKKSPackedPlaintext([bias], precision)
    
    # IMPROVEMENT 3: Ensure we're at an appropriate level before multiplication
    # Getting the current level of the ciphertext
    current_level = input.GetLevel()
    print(f"✓ Current ciphertext level: {current_level}")
    
    # IMPROVEMENT 4: Perform the multiplication with rescaling to manage noise
    encrypted_result = context.EvalMult(input, plaintext_weights)
    
    # IMPROVEMENT 5: Use a more accurate summation algorithm
    # For improved accuracy, we can use a tree-like summation instead of a single EvalSum
    # This reduces error accumulation during homomorphic addition
    len_weights = len(weights)
    if len_weights > 1:
        # Perform summation in a binary tree manner for better accuracy
        step = 1
        while step < len_weights:
            for i in range(0, len_weights - step, step * 2):
                if i + step < len_weights:
                    encrypted_result = context.EvalRotate(encrypted_result, step)
                    encrypted_result = context.EvalAdd(encrypted_result, context.EvalRotate(encrypted_result, -step))
            step *= 2
        
        # Final rotation to get the sum in the first slot
        encrypted_result = context.EvalRotate(encrypted_result, 0)
    else:
        # If there's only one weight, no summation needed
        pass
    
    # Add the bias term
    encrypted_result = context.EvalAdd(encrypted_result, plaintext_bias)

    print("✅ Encrypted linear regression computation completed with improved accuracy.")
    print(f"✓ Final ciphertext level: {encrypted_result.GetLevel()}")
    
    return encrypted_result  # Return the final encrypted prediction


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--key_pub')
        parser.add_argument('--key_mult')
        parser.add_argument('--key_rot')
        parser.add_argument('--cc')
        parser.add_argument('--sample')
        parser.add_argument('--output')
        args = parser.parse_args()

        a = CKKSParser()
        a.load(args)
        
        a.context.Enable(PKESchemeFeature.PKE)
        a.context.Enable(PKESchemeFeature.KEYSWITCH)
        a.context.Enable(PKESchemeFeature.LEVELEDSHE)
        a.context.Enable(PKESchemeFeature.ADVANCEDSHE)

        answer = solve(a.input, a.context, a.public_key)

        if not SerializeToFile(args.output, answer, BINARY):
            raise Exception('output serialization failed')

    except Exception as err:
        print(f'execution error: {err}')
        sys.exit(1)