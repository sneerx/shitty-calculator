
import sys

def calculator(first_number,second_number,islem):
        
   
        if islem == "+" :
            return (str(first_number) + str(islem) + str(second_number) + "=" + str(first_number+second_number)  )
            


        elif islem =="-":
            return (str(first_number) + str(islem) + str(second_number) + "=" + str(first_number-second_number)  )
        elif islem == "*":
            return (str(first_number) + str(islem) + str(second_number) + "=" + str(first_number*second_number)  )

        elif islem == "/":
            return (str(first_number) + str(islem) + str(second_number) + "=" + str(first_number/second_number)  )

        else:
            print("hatalı islem girisi.")


while True:
    islem = input("(+, -, *, / çıkmak için 'q') --> :")
    if islem =="q":
        sys.exit()
    sayi1 = float(input("first number: "))
    sayi2 = float(input("second number : "))
    

    print(calculator(sayi1,sayi2,islem))
    


    
             
        