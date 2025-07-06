#include "openfhe.h"
#include "ciphertext-ser.h"
#include "cryptocontext-ser.h"
#include "key/key-ser.h"
#include "scheme/ckksrns/ckksrns-ser.h"

using namespace lbcrypto;

class CKKSTaskSolver {
    CryptoContext<DCRTPoly> m_cc;
    PublicKey<DCRTPoly> m_PublicKey;
    Ciphertext<DCRTPoly> m_InputC;
    Ciphertext<DCRTPoly> m_OutputC;
    
    // Member variables need to be in the same order as they're initialized
    // in the constructor initialization list
    std::string m_CCLocation;
    std::string m_PubKeyLocation;
    std::string m_MultKeyLocation;
    std::string m_RotKeyLocation;
    std::string m_InputLocation;
    std::string m_OutputLocation;
    
    // Neural network implementation details (private to keep header matching template)
    int num_slots = 8192;
    std::vector<std::vector<double>> weights1;
    std::vector<double> bias1;
    std::vector<std::vector<double>> weights3;
    std::vector<double> bias3;
    double beta = 0.9485346674919128;
    double gamma = 0.4713829457759857;
    double y_mean = 0.0;
    double y_std = 1.0;
    
    // Helper methods
    void loadModelWeights();
    void loadPreprocessingParams();
    Plaintext encode(const std::vector<double> &vec, int level);
    std::vector<double> decrypt_to_vector(const Ciphertext<DCRTPoly> &c, int slots);
    Ciphertext<DCRTPoly> linear_layer(const Ciphertext<DCRTPoly> &input, 
                                     const std::vector<std::vector<double>> &weights, 
                                     const std::vector<double> &bias);
    Ciphertext<DCRTPoly> activation(const Ciphertext<DCRTPoly> &input);

public:
    CKKSTaskSolver(std::string ccLocation, std::string pubKeyLocation, std::string multKeyLocation,
                std::string rotKeyLocation,
                std::string inputLocation,
                std::string outputLocation);
    void initCC();
    void eval();
    void serializeOutput();
};