from credit import credit, exit_program, clear, about_us
import function_handler
from achievements import main as achievements
from glycerol_parta import main as glycerol_parta
from glycerol_partb import main as glycerol_partb
from motor_oil import main as motor_oil
from hydarulic_oil import main as hydarulic_oil
from combine_oil_graph import main as combine_oil_graph

while 1 == 1:
    achievements()

def main(exit_value):
    for i in range(10):
        print('\n')
    print('Choose mode:')
    print('1. Glycerol: Least-square graph of v against t')
    print('2. Glycerol: Least-square graph of v/t against 1/{t^2}')
    print('3. Motor Oil: Least-squares graph of log{log(v + 0.8)} against log(T)')
    print('4. Hydraulic Oil: Least-squares graph of log{log(v + 0.8)} against log(T)')
    print('5. Comparison of log{log(v + 0.8)} against log(T) for Motor and Hydraulic Oil')
    print('6. About Us')
    print('7. Credit')
    print('8. Achivement')
    print('9. Exit')
    print('\nCredit by: \nSek Yin Jia\n')
    print('Please insert the mode:')
    user_answer = input()
    
    # other output
    if "6" in user_answer:
        about_us()
    if "7" in user_answer:
        credit()
    if "8" in user_answer:
        achievements()
        # achivement
    if "9" in user_answer:
        exit_value = True
        exit_program()
        exit()
        return exit_value
    
    # function output
    clear()
    if "1" in user_answer:
        glycerol_parta()    
    if "2" in user_answer:
        glycerol_partb()
    if "3" in user_answer:
        motor_oil()
    if "4" in user_answer:
        hydarulic_oil()
    if "5" in user_answer:
        combine_oil_graph()
    return exit_value
    
    
exit_value = False
for i in range(10):
        print('\n')
print('Welcome to S3 Graph Analysis.')
print('Before we start make sure that you already insert your data on the csv files.\n\n\n')
input("\n\nPress Enter To Continue:\n")
while exit_value == False:
    exit_value = main(exit_value)