
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

exact_output=f"""my name is {name}, I am {age} years old

my skills are
 - {skill1} ({level1})
 - {skill2} ({level2})
 - {skill3} ({level3})

I am looking for a job with a salary of {lower}-{upper} euros per month"""

print(exact_output)