from turtle import Turtle,Screen
import pandas
import time
on=True
turtle=Turtle()
correct=Turtle()
correct.penup()
correct.hideturtle()
correct.color('green')
wrong=Turtle()
wrong.penup()
wrong.hideturtle()
wrong.color('red')
screen=Screen()
image='real africa.gif'
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv('African countries and co-ordinates.csv')

countries=data.country.to_list()
numbers=data.number.to_list()





while on:
    user_country_number = screen.numinput(title='Country Number', prompt='Enter the country number')
    country_data = data[data.number == user_country_number].country.to_list()[0]
    

    time.sleep(1)
    user_country=screen.textinput(title='Country Name',prompt='Enter the name of the selected country').title()

    if user_country==country_data:
        x_use = data[data.number == user_country_number].x.item()
        y_use = data[data.number == user_country_number].y.item()
        countries.remove(country_data)
        numbers.remove(data[data.country == country_data].number.item())
        correct.goto(x_use-1, y_use-13)
        correct.write(f'✓', font=('Arial', 10, 'bold'))


    if user_country=='Exit' or user_country_number==0:
        on=False


countries_to_study={
    'number':numbers,
    'country': countries
}

countries_to_study=pandas.DataFrame(countries_to_study)

countries_to_study.to_csv('countries_to_study.csv')




