import argparse
from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling

class Preprocessor:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    
    # The Task associated with this class. This is also the main class of the project.
    tasks = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = 0
    
    def __init__(self, input_file):
        self.data = DataInput().inputFunction(input_file)
        print("\n\n" + self.bold_start + "WELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\N{grinning face}" + self.bold_end + "\n\n")

    # function to remove the target column of the DataFrame.
    def removeTargetColumn(self):
        print("Columns\U0001F447\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        
        while(1):
            column = input("\nWhich is the target variable:(Press q to exit)  ").lower()
            if column == "q":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    self.data.drop([column], axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Try again......\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Try again with the correct column name...\U0001F974")
        return

    # main function of the Preprocessor class.
    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks (Preprocessing)\U0001F447\n")
            for task in self.tasks:
                print(task)

            while(1):
                choice = input("\nWhat do you want to do? (Press q to exit):  ").lower()
                if choice == "q":
                    exit()
                try:
                    choice = int(choice)
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            # moves the control into the DataDescription class.
            if choice==1:
                DataDescription(self.data).describe()

            # moves the control into the Imputation class.
            elif choice==2:
                self.data = Imputation(self.data).imputer()

            # moves the control into the Categorical class.
            elif choice==3:
                self.data = Categorical(self.data).categoricalMain()

            # moves the control into the FeatureScaling class.
            elif choice==4:
                self.data = FeatureScaling(self.data).scaling()

            # moves the control into the Download class.
            elif choice==5:
                Download(self.data).download()
            
            else:
                print("\nWrong Integer value!! Try again..\U0001F974")
                

def main():
    parser = argparse.ArgumentParser(
        description="ML Preprocessor CLI",
        add_help=False  # Disable default help to customize
    )
    parser.add_argument('-i', '--input', type=str, required=True, help='Input dataset file path')
    parser.add_argument('-h', '--help', '-help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit')
    args = parser.parse_args()

    obj = Preprocessor(args.input)
    obj.preprocessorMain()

if __name__ == "__main__":
    main()
