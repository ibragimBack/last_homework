from aiogram import Router,types, F
from aiogram.filters import Command

choice_router = Router()

@choice_router.message(Command('choice'))
async def chosen(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Боевик'),
                types.KeyboardButton(text='Комедия')
            ],
            [
                types.KeyboardButton(text='Романтика'),
                types.KeyboardButton(text='Мистика')
            ],
            [
                types.KeyboardButton(text='Фэнтези'),
                types.KeyboardButton(text='Приключения')
            ]
        ]
    )
    await message.answer(f'{message.from_user.first_name} выберите жанр', reply_markup=kb)


@choice_router.message(F.text.lower() == 'боевик')
async def information(message: types.Message):
    await message.answer('''
    Боевик — жанр, в котором основное предпочтение отдается погоням, экшену, а не 
    сюжету. Как правило, в фильмах этого жанра есть один положительный герой и много 
    отрицательных. Часто изображается борьба добра со злом и часто добро оказывается  
    сильнее зла.''')


@choice_router.message(F.text.lower() == 'романтика')
async def information(message: types.Message):
    await message.answer('''
    Романти́ческий фильм — кинематографический жанр, который сосредоточен на страсти, 
    эмоциях и романтических переживаниях главных героев и истории их любви, которая 
    может проходить через свидания, ухаживания и брак.''')


@choice_router.message(F.text.lower() == 'комедия')
async def information(message: types.Message):
    await message.answer('''
    Комедия - жанр художественного произведения, характеризующийся юмористическим или
    сатирическим подходами, и также вид драмы, в котором специфически разрешается 
    момент действенного конфликта или борьбы.''')


@choice_router.message(F.text.lower() == 'приключения')
async def information(message: types.Message):
    await message.answer('''
    Приключе́ние — захватывающее происшествие, неожиданное событие или случай в жизни, 
    цепь нечаянных событий и непредвиденных случаев; нежданная быль, замечательное свершение,
    волнующее похождение, интересное испытание, возбуждающий переворот или любовная авантюра.''')


@choice_router.message(F.text.lower() == 'фэнтези')
async def information(message: types.Message):
    await message.answer('''
    Фэнтези — фантастический жанр, который использует мифологические и фольклорные, а также
    сказочные мотивы в повествовании. В связи с тем, что жанр фэнтези формировался под влиянием
    британских авторов, в первую очередь, под влиянием Дж. Р. Р.''')


@choice_router.message(F.text.lower() == 'мистика')
async def information(message: types.Message):
    await message.answer('''
    Мистический фильм или мистика — кинематографический жанр, часто включающий в себя элементы
    фантастики и фэнтези. В основе сюжетов мистических фильмов лежит взаимодействие персонажей
    из реального мира с миром потусторонних сил и явлений.''')