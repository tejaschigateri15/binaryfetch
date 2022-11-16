import smtplib,ssl


def sendMAIL(re):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    sender_email = "tejaschigateri15@gmail.com"
    password = "ykbrjkgbdamyxult"

    port = 587
    smtp_server = "smtp.gmail.com"

    message = """\
    Subject:HEALTH UPDATES\n
    We appreciate that you connected with us.
    From now on you will be receiving weekly health updates based on your diseases and you will be also receiving the diet plans.
    \n\nFor further queries contact our experts through email and phone(+91 1234567890).
    
    
    Thank You """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, re, message)


print("-----welcome to python chatbot-----")

name = input('enter your name : ')
age = int(input('enter your age : '))
re = input("Enter email=")
n=input("Do you want to recieve updates(y/n)?")


print("Welcome " + name + ", we are here to help you with your diets")
print("")
print("1.Blood Pressure")
print("2.Night Blindness")
print("3.Diabetes")
print("4.Rickets")
print("5.Goiter")
print("6.Anemia")

print("")
disease = int(input("Select you disease among the give list: "))
if disease == 1:
    print("")
    message = "The main reason for BP is due to unhealthy lifestyle choices, such as not getting regular physical " \
              "activity.\n" \
              "High blood pressure can often be prevented or reduced by eating healthily,\n" \
              "maintaining a healthy weight, taking regular exercise, drinking alcohol in moderation and not " \
              "smoking\n\n" \
              "Best foods for high blood pressure :" \
              "\n1. Citrus fruits \n \nIncluding grapefruit, oranges, and lemons, may have powerful " \
              "blood-pressure-lowering " \
              "effects. \n They’re loaded with vitamins, minerals, and plant compounds that may help keep your heart " \
              "healthy " \
              "by reducing heart disease risk factors like high blood pressure" \
              "\n2. Salmon and other fatty fish" \
              "\nFatty fish are an excellent source of omega-3 fats, which have significant heart health benefits. " \
              "\nThese " \
              "fats may help reduce blood pressure levels by reducing inflammation and \ndecreasing levels of " \
              "blood-vessel-" \
              "constricting compounds called oxylipins" \
              "\n3. Beans and lentils" \
              "\nBeans and lentils are rich in nutrients that help regulate blood pressure, such as fiber, magnesium, " \
              "and" \
              "potassium. \nNumerous studies have shown that eating beans and lentils may help lower high blood " \
              "pressure levels. "
    print(message)




elif disease == 2:
    print("")
    print(
        "The main reason for night blindness is  The most common kinds of color blindness are genetic, meaning they're passed down from parents.")
    print(
        "1. Green \n\n Green colored foods like peas, kale, spinach, honeydew melons, kiwifruit, dark leafy lettuces, and \nleafy greens contain lutein which helps maintain good vision and can help reduce the risk of macular degeneration and cataracts.")
    print("\n2. Yellow")
    print(
        "\n The yellow orange colored food are high in bioflavonoids, which work in combination with vitamin C to help reduce the risk of cancer and heart attack. ")
    print(
        "\n3. Orange \n\n Dark orange foods like pumpkin, sweet potatoes, apricots, peaches, carrots, cantaloupes, mangoes, \nand butternut squash contain beta-carotene, a powerful antioxident that can help keep your immune system healthy")


elif disease == 3:
    print("")
    print(" Your food choices matter a lot when you've got diabetes.")
    print("Starches :")
    print("Your body needs carbs. But you want to choose wisely. Use this list as a guide.")
    print("")
    print("Prevention:")
    print("1.Lose extra weight")
    print("2.Be more physically active")
    print("3. Eat healthy plant foods")
    print("4.Quit smoking if you are a current tobacco user")
    print("")
    print("Best Choices :")
    print("1. Whole grains, such as brown rice, oatmeal, quinoa, millet, or amaranth")
    print("2. Baked sweet potato")
    print("3. Items made with whole grains and no (or very little) added sugar")

elif disease == 4:
    print("")
    print("A lack of vitamin D or calcium is the most common cause of rickets. "
          "Vitamin D largely comes from exposing the skin to sunlight, "
          "but it's also found in some foods, such as oily fish and eggs.")

    print("Vitamin D deficiency can lead to a loss of bone density, "
          "which can contribute to osteoporosis and fractures (broken bones).")
    print(" not to worry most cases of rickets (especially nutritional rickets) are curable when caught early. "
          "In most cases, changes to diet, added vitamin supplements and more sunlight exposure are enough to cure this disease.")
    print("")
    print(
        "Depending on how severe the case is, your pediatrician may recommend one or more of the following treatments for rickets:")
    print("DIET CHANGES: This usually involves high doses of vitamin D, from either diet or supplements. "
          "These doses may be given for several months, depending on the severity of the case and other factors. "
          "Your pediatrician may also recommend a standard daily vitamin D supplement once the higher doses aren’t needed.")
    print("SUNLIGHT: Because your body can naturally make vitamin D when you’ve been exposed to sunlight, "
          "encouragement to get outside and get some sunshine is likely.")
    print("SURGERY: Usually, your child’s bones will straighten out on their own. "
          "For especially severe cases, children may need to wear braces to help correct the bending of their bones. "
          "In some  rare cases, surgery may also be an option.")

elif disease == 5:
    print("")
    print(
        "Goiter may be associated with an irregular amount of thyroid hormone in your body (hyperthyroidism or hypothyroidism) or")
    print("with normal levels of thyroid hormone (euthyroid).")
    print(
        "Anyone can have a goiter, but it’s about four times more likely to develop in people assigned female at birth "
        "compared to people assigned male at birth.")
    print("")
    print("Prevention:")
    print(
        "A goiter caused by iodine deficiency (simple goiter) is generally the only type of goiter you can prevent. Consuming a diet that includes fish, "
        "dairy and a healthy amount of iodized table salt prevents these types of goiters.")
    print("")
    print("Treatment:")
    print("Medications: Levothyroxine (Levothroid®, Synthroid®) is a thyroid hormone replacement therapy. "
          "These drugs include methimazole (Tapazole®) and propylthiouracil. ")
    print(
        "Radioactive iodine treatment: This treatment, used in cases of an overactive thyroid gland, involves taking radioactive iodine orally. "
        "The iodine goes to your thyroid gland and kills thyroid cells, which shrinks the gland. After radioactive iodine treatment, "
        "you’ll likely need to take thyroid hormone replacement therapy for the rest of your life.")
    print("Surgery: Your provider may recommend surgery to remove all or part of your thyroid gland (thyroidectomy). "
          "You may need surgery if the goiter is large and causes problems with breathing and swallowing.")

elif disease == 6:
    print(
        "most common type of anemia is caused by a shortage of iron in your body. Your bone marrow needs iron to make hemoglobin. \n",
        "Without adequate iron, your body can't produce enough hemoglobin for red blood cells. ")
    print("")
    print("You can’t prevent some kinds of anemia, such as sickle cell anemia, hemolytic anemia or aplastic anemia.\n",
          " People with chronic diseases who may develop anemia should watch for anemia symptoms.\n",
          " And you can prevent nutritional anemias by eating a healthy diet.")
    print("")
    print("If nutritional deficiencies are responsible for anemia, eating more iron-rich foods can help.")
    print(
        " 1.leafy green vegetables \n 2.Kale \n 3.Spinach \n 4.Watercress,pulses and beans\n 5.Brown rice \n 6.white or red meats\n 7.nuts and seeds")

if (n=='y'):
    sendMAIL(re)
