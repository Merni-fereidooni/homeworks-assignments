import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="/* create a emotion recognition software that detects emotions through eyes only in real time and has access to computer webcam and phone selfie camera: */\n\n#include <opencv2/core/core.hpp>\n#include <opencv2/highgui/highgui.hpp>\n#include <opencv2/imgproc/imgproc.hpp>\n#include <opencv2/objdetect/objdetect.hpp>\n#include <opencv2/ml/ml.hpp>\n#include <iostream>\n#include <fstream>\n#include <sstream>\n#include <stdio.h>\n#include <stdlib.h>\n#include <string>\n#include <vector>\n#include <math.h>\n#include <time.h>\n#include <dirent.h>\n#include <sys/types.h>\n#include <sys/stat.h>\n#include <unistd.h>\n#include <errno.h>\n#include <cstdlib>\n#include <cstdio>\n#include <cstring>\n#include <cmath>\n#include <ctime>\n#include <cassert>\n#include <cctype>\n#include <cfloat>\n#include <climits>\n#include <cstdarg>\n#include <cstddef>\n#include <cstdio>\n#include <cstdlib>\n#include <cstring>\n#include <ctime>\n#include <algorithm>\n#include <bitset>\n#include <complex>\n#include <deque>\n#include <exception>\n#include <fstream>\n#include <functional>\n#include <iomanip>\n#include <ios>\n#include <iosfwd>\n#include <iostream>\n#include <istream>\n#include <iterator>\n#include <limits>\n#include <list>\n#include <locale>\n#include <map>\n#include <memory>\n#include <new>\n#include <numeric>\n#include <ostream>\n#include <queue>\n#include <set>\n#include <sstream>\n#include <stack>\n#include <stdexcept>\n#include <streambuf>\n#include <string>\n#include <typeinfo>\n#include <utility>\n#include <valarray>\n#include <vector>\n#include <array>\n#include <atomic>\n#include <chrono>\n#include <condition_variable>\n#include <forward_list>\n#include <future>\n#include <initializer_list>\n#include <mutex>\n#include <random>\n#include <ratio>\n#include <regex>\n#include <scoped_allocator>\n#include <system_error>\n#include <thread>\n#include <tuple>\n#include <typeindex>\n#include <type_traits>\n#include <unordered_map>\n#include <unordered_set>\n#include <bits/stdc++.h>\n\nusing namespace std;\nusing namespace cv;\n\n/*\n\n// create a function that detects the face and eyes in a given image:\n\nvoid detectAndDisplay(Mat frame)\n{\n    std::vector<Rect> faces;\n    Mat frame_gray;\n    Mat crop;\n    Mat res;\n    Mat gray;\n    string text;\n    stringstream sstm;\n\n    cvtColor(frame, frame_gray, COLOR_BGR2GRAY);\n    equalizeHist(frame_gray, frame_gray);\n\n    // Detect faces\n    face_cascade.detectMultiScale(frame_gray, faces, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));\n\n    // Set Region of Interest\n    cv::Rect roi_b;\n    cv::Rect roi_c;\n\n    size_t ic = 0; // ic is index of current element\n    int ac = 0; // ac is area of current element\n\n    size_t ib = 0; // ib is index of biggest element\n    int ab = 0; // ab is area of biggest element\n\n    for (ic = 0; ic < faces.size(); ic++) // Iterate through all current elements (detected faces)\n\n    {\n        roi_c.x = faces[ic].x;\n        roi_c.y = faces[ic].y;\n        roi_c.width = (faces[ic].width);\n       ",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
