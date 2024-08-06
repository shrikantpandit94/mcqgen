Hello

To create vir env - conda create -p venv python=3.10 -y 
To install requirements - pip install -r requirements.txt

To activate local environment - source activate ./venv  
                                conda activate /workspaces/mcqgen/venv
                                conda deactivate
To run on Streamlit - streamlit run StreamlitAPP.py/ streamlit run your_script.py

For AWS EC2 instance:
Login | Config Ubuntu machine | Launch instance
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar sudo vim wget -y
git clone https://github.com/shrikantpandit94/mcqgen

[[[ ls
cd mcqgen
Within mcqgen --> ls
add openai api key -->touch .env
check key --> ls -a
open vi editor --> vi .env | to get out --> .wq
to check --> cat .env ]]]

[[[ if you want to add openai api key
create .env file in your server --> touch.env
vi.env
press insert
copy your api key and paste it there
press and then :wq and hit enter ]]]

install --> sudo install python3-pip| pip3 install -r requirements.txt 
install streamlit --> python3 -m streamlit run StreamlitAPP.py

Edit EC2 security rules
Open instance --> Security --> Security group --> Inbound rules --> Edit inbound rules --> Add <Type>Custom TCP , <Port> 8501, <Source>Anywhere



