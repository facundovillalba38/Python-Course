# App to sort the datatypes of diferent lists

str_list = ['1', '200', '20', '100']
print("Str list contains the elements: ", str_list)
print("Str list datatype: ",type(str_list))
print("The element",str_list[0],"is a",type(str_list[0]),"\n")

int_list = [1, 200, 20, 100]
print("Int list contains the elements: ", int_list)
print("Int list datatype: ",type(int_list))
print("The element",int_list[0],"is a",type(int_list[0]),"\n")


float_list = [1.25, 2.4,1.1,2.33]
int_list = [1, 200, 20, 100]
print("Float list contains the elements: ", float_list)
print("Float list datatype: ",type(float_list))
print("The element",float_list[0],"is a",type(float_list[0]),"\n")

str_list.sort()
int_list.sort()

print("Sorted str list",str_list)
print("Sorted int list",int_list)