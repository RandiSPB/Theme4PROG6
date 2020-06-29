# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

3. Посчитайте долю погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

"""
import pandas

parsed_csv = pandas.read_csv('train.csv', sep=',', index_col='PassengerId', quotechar='"')


def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на пароходе? Приведите два числа через пробел.
    """
    return data['Sex'].value_counts()


def get_port_distrib(data):
    """  
    2. Подсчитайте, сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port = data['Embarked'].value_counts()
    return port['S'], port['Q'], port['C']


def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на пароходе (число и процент).
    """
    died, survived = data['Survived'].value_counts()
    survival_ratio = (survived / (survived + died)) * 100
    dying_ratio = (died / (survived + died)) * 100
    return survived, survival_ratio, died, dying_ratio


def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    ticket_class = data['Pclass'].value_counts()
    first_class, second_class, third_class = ticket_class
    first_class_ratio = (first_class / sum(ticket_class)) * 100
    second_class_ratio = (second_class / sum(ticket_class)) * 100
    third_class_ratio = (third_class / sum(ticket_class)) * 100
    class_stats = (
            first_class, first_class_ratio,
            second_class, second_class_ratio,
            third_class, third_class_ratio
            )
    return class_stats


def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    return data['SibSp'].corr(data['Parch'], method='pearson')


def find_corr_age_survival(data):
    """
    6.1. Выясните, есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - возрастом и параметром survival;
    """
    return data['Survived'].corr(data['Age'], method='pearson')


def find_corr_sex_survival(data):
    """
    6.2. Выясните, есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - полом человека и параметром survival;
    """
    gender_df = pandas.Series([1 if i == 'male' else 0 for i in data['Sex']])
    return data['Survived'].corr(gender_df, method='pearson')


def find_corr_class_survival(data):
    """
    6.3. Выясните, есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - классом, в котором пассажир ехал, и параметром survival.
    """
    return data['Survived'].corr(data['Pclass'], method='pearson')


def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """
    avg_age = parsed_csv['Age'].mean(skipna=True)
    median_age = parsed_csv['Age'].median(skipna=True)
    return avg_age, median_age


def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """
    avg_fare = parsed_csv['Fare'].mean(skipna=True)
    median_fare = parsed_csv['Fare'].median(skipna=True)
    return avg_fare, median_fare


def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    names = [i.split(', ')[1] for i in parsed_csv['Name']]
    sorted_names = pandas.Series(names).value_counts()
    return sorted_names.index[0], sorted_names.iat[0]


def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    older_male = parsed_csv[(parsed_csv['Age'] > 15) & (parsed_csv['Sex'] == 'male')]
    older_female = parsed_csv[(parsed_csv['Age'] > 15) & (parsed_csv['Sex'] == 'female')]

    male_names = [i.split(', ')[1] for i in older_male['Name']]
    male_sorted_names = pandas.Series(male_names).value_counts()

    female_names = [i.split(', ')[1] for i in older_female['Name']]
    female_sorted_names = pandas.Series(female_names).value_counts()
    return male_sorted_names.index[0], male_sorted_names.iat[0], female_sorted_names.index[0], female_sorted_names.iat[0]


def test_get_number_of_pass():
    assert get_sex_distrib(parsed_csv) == (577, 314), "Количество мужчин и женщин на Титанике"


def test_get_number_embarked():
    assert get_sex_distrib(parsed_csv) == (644, 77, 168), "Количество пассажиров в разных портах на Титанике"

# аналогично протестировать остальные функции


print('-----\n1. gender\nmale: {}\nfemale: {}'.format(*get_sex_distrib(parsed_csv)))

print('-----\n2. embarked')
print('southampton: {}; queenstown: {}; cherbourg: {}'.format(*get_port_distrib(parsed_csv)))

print('-----\n3. survival percent')
print('survived: {} ({:.2f}%)\ndied: {} ({:.2f}%)'.format(*get_surv_percent(parsed_csv)))

print('-----\n4. class stats')
print('1: {} ({:.2f}%)\n2: {} ({:.2f}%)\n3: {} ({:.2f}%)'.format(*get_class_distrib(parsed_csv)))

print('-----\n5. siblings-kids correlation')
print('correlation: {}'.format(find_corr_sibsp_parch(parsed_csv)))

print('-----\n6.1. age-survival correlation')
print('correlation: {}'.format(find_corr_age_survival(parsed_csv)))

print('-----\n6.2. gender-survival correlation')
print('correlation: {}'.format(find_corr_sex_survival(parsed_csv)))

print('-----\n6.3. class-survival correlation')
print('correlation: {}'.format(find_corr_class_survival(parsed_csv)))

print('-----\n7. avg & median age')
print('average age: {}\nmedian age: {}'.format(*find_pass_mean_median(parsed_csv)))

print('-----\n8. avg & median ticket fare')
print('average fare: {}\nmedian fare: {}'.format(*find_ticket_mean_median(parsed_csv)))

print('-----\n9. the most popular male name')
print('the most popular male name is {} ({})'.format(*find_popular_name(parsed_csv)))

print('-----\n10. the most popular >15yo name')
print('male: {} ({})\nfemale: {} ({})'.format(*find_popular_adult_names(parsed_csv)))
