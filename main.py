from load_in import load_in
from user_input import user_input
from calculator import build_summary
from summary_report import summary_report

def main():

    load_in()
    user = user_input()
    summary = build_summary(user)
    summary_report(user, summary)
   
if __name__ == "__main__":
      main()