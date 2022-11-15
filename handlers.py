from aiogram import Dispatcher
import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.set_total_candies, commands=['set'])
    dp.register_message_handler(commands.one_move, commands=['set_move'])
    dp.register_message_handler(commands.help, commands=['help'])
    