#include <iostream>
#include <gflags/gflags.h>
#include "easylogging++.h"
using namespace std;

INITIALIZE_EASYLOGGINGPP

DEFINE_bool(big_menu, true, "Include 'advanced' options in the menu listing");

int main(int argc, char *argv[]) {
  ::google::ParseCommandLineFlags(&argc, &argv, true);
  LOG(INFO) << "My first info log using default logger";
  cout << FLAGS_big_menu << endl;
  if (FLAGS_big_menu) {
    cout << "Hello World!" << endl;
  } else {
    cout << "Sorry!" << endl;
  }
  return 0;
}










