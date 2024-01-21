import argparse
from colored import fg, attr
import review
import subprocess

def print_colored(text, color):
    print(f"{fg(color)}{text}{attr(0)}")

def main():
    
    subprocess.run('cls',shell=True)
    
    parser = argparse.ArgumentParser(description='Your SENIOR .py - Your senior developer to review your code.')
    parser.add_argument('--i', help='Input file path')
    parser.add_argument('--api', help='Your Gemini API Key')
    parser.add_argument('-d',help='Generate Review in detail')
    parser.add_argument('-s',help='Generate Review in short')

    args = parser.parse_args()

    # Print header
    print_colored("Your SENIOR .py - Reviewing your {stupid-code}...", 'blue')
    
    # Check if the 'i' argument is provided
    if args.i:
        input_file_path = args.i
        print_colored(f"Input file path: {input_file_path}",'green')
        # Add your code logic here for handling the input file

    # Check if the 'api' argument is provided
    if args.api:
        gemini_api_key = args.api
        print_colored(f"Gemini API Key: {gemini_api_key}",'red')
        # Add your code logic here for handling the Gemini API Key
    
    if args.d :
        print_colored("Review in Detail",'green')
        try :
            review_out = review.generate_review_in_detail(args.api,args.i)
            print_colored(f"Review/Analysis : {review_out}",'cyan')
        except Exception:
            print_colored('Failed to generate review , please try again or check everything again...','red')
    
    print_colored("Reviewing your stupid code ...",'yellow')
    
    # Call output from gemini_api 
    if args.s :
        print_colored("Review in Short",'green')
        try :
            review_out = review.generate_review(args.api,args.i)
            print_colored(f"Detailed Review/Analysis : {review_out}",'cyan')
        except Exception:
            print_colored('Failed to generate review , please try again or check everything again...','red')
    

if __name__ == "__main__":
    main()
