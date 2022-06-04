Challenge Name: ReverseScript
Date: 4 June 2022
Challenge Author(s): ERr0rhm3

### Description:

az = a, Az = a, aZ = a, zA = a, Za = a, AZ = A, ZA = A

### Objective

To find the flag by reverse engineering a given bin file.

### Difficulty:

'Medium`

### Flag:

'THM{doEstHeflAgalwaayShavetOmEaNsomethIng}`

# Writeup

1) I find a RevScript.bin file. Upon running the file command it shows that it is an ELF executible file.
![image](https://user-images.githubusercontent.com/61114467/171992079-14708329-1790-4afd-b1ac-743bf47923b5.png)

2) Since it's a binary, i'll run it. Upon running it, it takes a user input and does a string match.
![image](https://user-images.githubusercontent.com/61114467/171992150-9f26eedd-6708-4323-abaf-7e5f48fb8059.png)

3) I'll use radare2 for reversing the binary. Upon running the afl command. I see a main function. Ill see its contents. There is a string declaration before the program asks for user input. 
![image](https://user-images.githubusercontent.com/61114467/171992280-e06ac25a-81fd-473e-9b7f-c4071b23e60b.png)

4) Upon copying the string and providing the program with the string, it dishes out some gibberish.
![image](https://user-images.githubusercontent.com/61114467/171992332-62991b9e-f492-48c2-af13-b207a77b5792.png)

5) From the description, it looks like the sum of the corresponding numbers of two characters is being used to is used to get a character. a=1, z=26 a+z=27. Upon dividing 27/26, the remainder is 1, so it is converted to a. if both the paired characters are in uppercase, resultant character will be in uppercase, otherwise the resultant character will be in lowercase. I wrote a python script to do that. The code provided here can also be used https://github.com/gaurav16-byte/Stupid_Encoding_Algorithm/blob/main/STUPID%20ENCODING%20ALGORITHM.py
![image](https://user-images.githubusercontent.com/61114467/171992516-2a64125b-1b12-4f6f-803c-955ea43b1dc6.png)

6) Upon running the script, the decoded string appears like this: doEstHeflAgalwaayShavetOmEaNsomethIng. This looks like the flag. I will enclose this in the THM{} manner. 
THM{doEstHeflAgalwaayShavetOmEaNsomethIng} and submit it.

7) Challenge Solved!