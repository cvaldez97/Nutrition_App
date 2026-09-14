from load_in import load_in
from user_input import user_input
from summary_report import summary_report

def main():

    load_in()
    user = user_input()
    summary_report(user)
   
if __name__ == "__main__":
      main()