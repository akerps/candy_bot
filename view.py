from aiogram import types
from create_bot import bot

async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет! '
                                       f'Сегодня будем делить конфеты!\n'
                                       f'Для вызова подсказки воспользуйся командой /help')
    
async def help_message(message: types.Message):
    await bot.send_message(message.from_user.id, '/start - начало игры,\n'
                           '/set (цифра без скобок)- изменение общего количества конфет,\n'
                           '/set_move (цифра без скобок)- изменение количества конфет, которые можно взять за один ход')                                                   

    
async def remainder_player(message: types.Message, pl_take, total):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name} взял {pl_take},'
                                                        f' и на столе осталось {total}')
    
async def player_win(message: types.Message):
    await bot.send_message(message.from_user.id, f'Победил {message.from_user.first_name}!')
    
    
async def too_much(message: types.Message):
    await bot.send_message(message.from_user.id, 'А не многовато ли взял?')
    
async def negative_amount(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ты не отдавай, а бери конфеты!')

async def null_amount(message: types.Message):
    await bot.send_message(message.from_user.id, 'Возьми хоть сколько-нибудь, не стесняйся!')   
    
async def mistake(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, вообще-то, конфеты мы считаем в цифрах!')
    
  
async def remainder_bot(message: types.Message, enemy_take, total):
    await bot.send_message(message.from_user.id, f'Бот взял {enemy_take},'
                                                            f' и на столе осталось {total}')
    
    
async def looser(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, ты проиграл,'
                                f'тебя дёрнула железяка!')
    
    
async def take_max(message: types.Message, max_take):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, бери конфеты, но не больше {max_take}!')
    
   
async def change_max(message: types.Message, count):
    await bot.send_message(message.from_user.id, f'Максимальное количество конфет изменили на {count}')


async def count_candy(message: types.Message, count):
    await bot.send_message(message.from_user.id, f'Теперь за один ход можно взять {count} конфет!')
