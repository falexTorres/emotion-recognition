#                               __                    __             
#                              /\ \__                /\ \__          
#   ___    ___     ___     ____\ \ ,_\    __      ___\ \ ,_\   ____  
#  /'___\ / __`\ /' _ `\  /',__\\ \ \/  /'__`\  /' _ `\ \ \/  /',__\ 
# /\ \__//\ \L\ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_/\ \/\ \ \ \_/\__, `\
# \ \____\ \____/\ \_\ \_\/\____/ \ \__\ \__/.\_\ \_\ \_\ \__\/\____/
#  \/____/\/___/  \/_/\/_/\/___/   \/__/\/__/\/_/\/_/\/_/\/__/\/___/  .txt
#
#

# CASC_PATH = './haarcascade_files/haarcascade_eye.xml'
CASC_PATH = './haarcascade_files/haarcascade_frontalface_default.xml'
SIZE_FACE = 48
EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
SAVE_DIRECTORY = './data/'
SAVE_MODEL_FILENAME = 'Gudi_model_100_epochs_20000_faces'
# SAVE_DATASET_IMAGES_FILENAME = './data_set_fer2013.npy'
# SAVE_DATASET_LABELS_FILENAME = './data_labels_fer2013.npy'
# SAVE_DATASET_IMAGES_TEST_FILENAME = './test_set_fer2013.npy'
# SAVE_DATASET_LABELS_TEST_FILENAME = './test_labels_fer2013.npy'
# SAVE_DATASET_IMAGES_FILENAME = './fer_final_dataset/fer_X_train_final.npy'
# SAVE_DATASET_LABELS_FILENAME = './fer_final_dataset/fer_y_train_final.npy'
# SAVE_DATASET_IMAGES_TEST_FILENAME = './fer_final_dataset/fer_X_test_smooth.npy'
# SAVE_DATASET_LABELS_TEST_FILENAME = './fer_final_dataset/fer_y_test.npy'
SAVE_DATASET_IMAGES_FILENAME = './train_set.npy'
SAVE_DATASET_LABELS_FILENAME = './train_labels.npy'
SAVE_DATASET_IMAGES_TEST_FILENAME = './test_set.npy'
SAVE_DATASET_LABELS_TEST_FILENAME = './test_labels.npy'