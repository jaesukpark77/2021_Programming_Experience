student_tuple = [('211101', '강이안', '010-123-1111'), ('2111102', '박동민', '010-123-2222'), ('211103', '강수정', '010-123-3333')]

student_dic = {}

for student in student_tuple:
    number, name, phone = student
    student_dic[number] = [name, phone]

for key, value in student_dic.items():
    print(key + " :", value[0])

number = input("학번을 입력하시오 : ")
print(number + '학생은' + student_dic[number][0] + '이며, 전화번호는' + student_dic[number][1] + '입니다.')