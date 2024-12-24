import sys
global credit, clear, exit_program, about_us

def credit():
    clear()
    print('Credit by: \nSek Yin Jia')
    print('Students Body Officer\nSecretary of Finance Office\nUniversity Malaya Students\' Union 24/25')
    input('\nMedia Officer\nPresidential Office\nUniversity Malaya Students\' Union 24/25')
    clear()
    print('𓆰♕𓆪\tProject Advisor: Tang Euzine')
    print('♕\tDeputy Project Advisor: Lim Zhi Wei')
    print('')
    print('✯ ✯ ✯ ✯\tProject Director: Sek Yin Jia')
    print('')
    print('✯ ✯ ✯\tDeputy Project Director (Management): Liu Jie Fei')
    input('✯ ✯ ✯\tDeputy Project Director (Execution): Lee Man Bin')
    print('')
    print('✯ ✯\tSenior Assistant Project Director (General Affairs): Albert Kwang')
    print('✯ ✯\tSenior Assistant Project Director (Finance): Pheonix Cheong')
    print('✯ ✯\tSenior Assistant Project Director (Planning): Olivia Ong Chen Ling')
    print('✯ ✯\tSenior Assistant Project Director (Strategic): Chan Hi Nin')
    print('')
    print('✯\tAssistant Project Director (General Affairs): Cheah Jin Yi')
    print('✯\tAssistant Project Director (Finance): Li Yi Lin')
    print('✯\tAssistant Project Director (Planning): Siau Zhi Xun')
    input('✯\tAssistant Project Director (Strategic): Samantha')
    print('')
    print('❁ ❁ ❁\tChief Project Executive:')
    print('')
    input('\n'.join([
        '\t'.join(['Angellice Ling','Tiffany Sim']),
        '\t'.join(['Stephanie Siew','Goh Yu Chen']),
        '\t'.join(['Tan Jia Jian','Khor Yan Ru']),
        '\t'.join(['Goh Chin Seong','Lim Zhi Wei']),
        '\t'.join(['Ang Sheng Jun','Ang Eng Jin'])
        ]))
    print('')
    print('┃ ❁ ❁\tSenior Project Executives:')
    print('')
    print('\n'.join([
        '\t'.join(['Sim Gui Shing','Leong Shi Jie','Cheah Xin Ru','Teo Sing Fang']),
        '\t'.join(['Pang Ke Xin','Phang Wei Jie','Tan Zhi Jian','Ooi Hui En']),
        '\t'.join(['Felicia Tan','Nga Kor Min','Tiger Hu','Lee Shi Min']),
        '\t'.join(['Ku Kian Xiang','Chan Wei Lun','Yong Tek Hua','Tan Chin Hong']),
        '\t'.join(['Yang Bbhg Dato Rick Cheng Wei Sung','Cheng Zheng Kai','Cheng Zheng Paul','Liu Xiao Tong'])
        ]))
    print('')
    print('❁ ❁\tAll Project Executives')
    print('')
    input('❁\tAll Junior Project Executives')
    print('')
    print('❀\tAll Assistant Project Assistants')
    print('')
    print('❮❮❮\tAll Chief Project Assistants')
    print('')
    print('❮\tAll Senior Project Assistants')
    print('')
    print('\tAll Project Assistants')
    print('')
    print('')
    print('')
    input('We Serve with Pride and Care\n\n\n')
    
    
def clear():
    for i in range(10):
        print('\n')

def exit_program():
    clear()
    input('Thank you for using my program.\nCome and join our Secretary of Finance Office UMSU 24/25\nWe want you!\n\nAny queries please contact Sek Yin Jia\nemail: yinjiasek@gmail.com\ntel: +6013-4540120')
    credit()

def about_us():
    clear()
    list = [
        "Moto",
        "Vision and Mision",
        "Top Management",
        "Exit"
    ]
    print("Please select the mode you want")
    for i in range(len(list)):
        print(i+1,". ",list[i])
    user_answer = input()
    if "1" in user_answer:
        clear()
        input("Our Moto:\n\n\nWe Serve with Pride and Care\n\n\n")
    if "2" in user_answer:
        clear()
        print("Our Vision:\n\n\nNo Working Days\n\n\n")
        input("Our Mision:\n\n\nMake Your Life Easier\n\n\n")
    if "3" in user_answer:
        clear()
        print('The Top Management')
        print('𓆰♕𓆪\tProject Advisor: Tang Euzine')
        print('')
        print('♕\tDeputy Project Advisor: Lim Zhi Wei')
        print('')
        print('')
        print('✯ ✯ ✯ ✯\tProject Director: Sek Yin Jia')
        print('')
        print('')
        print('✯ ✯ ✯\tDeputy Project Director (Management): Liu Jie Fei')
        print('')
        input('✯ ✯ ✯\tDeputy Project Director (Execution): Lee Man Bin')
    if "4" in user_answer:
        print()
        return None
        
    about_us()


