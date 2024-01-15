
##  Jinja2 Basics  ##     [] {} =



Jinja2 Docs:

    https://jinja.palletsprojects.com/en/3.1.x/


Templating allows you to use defined variables, rather than 
hard-coding values.


# Common String Manipulations 

   - upper
   - lower
   - title
   - replace
   - default

   Ex:
        {{ my_name | upper }}
        {{ my_name | replace ("Bond", "Bourne") }}
        {{ my_name | default("Bob") }}


# List & Set Based Filters

    - min
    - max
    - unique
    - union
    - intersect
    - random
    - join

    Ex:

        {{ 100 | random }}                 --->  46
        {{ [1, 2, 3] | max }}              --->  3
        {{ [1,2,3,2] | unique }}           --->  [1, 3]
        {{ [1,2,3,4] | union([4,5]) }}     --->  [1, 2, 3, 4, 5]
        {{ [1,2,3,4] | intersect([4,5]) }} --->  4
        {{ ["How", "are", "you"] | join(" ") }}  ---> "How are you"


# Loops

    {% for number in [1,2,3,4] %}
    {{ number }}
    {% endfor %}    --> 0 1 2 3 4


# Conditions

    {% for number in [1,2,3,4] %}
        {% if number == 2 %}
    {{ number }}
        {% endif %}
    {% endfor %}


