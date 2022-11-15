import asyncio, random, view, model
from create_bot import dp
from aiogram import types

async def start(message: types.Message):
    await view.hello(message)
    await asyncio.sleep(2)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn:
        await await_player(message)
    else:
        await enemy_turn(message)


async def player_turn(message: types.Message):
    max = model.get_max_take()
    if (message.text).isdigit():
        if 0 < int(message.text) <= max:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await view.remainder_player(message, player_take, total)
            if model.check_win(total):
                await view.player_win(message)
                return
            model.set_total_candies(total)
            await enemy_turn(message)
        elif int(message.text) < 0:
            await view.negative_amount(message)
        elif int(message.text) == 0:
            await view.null_amount(message)
        else:
            await view.too_much(message)
    else:
        await view.mistake(message)

async def enemy_turn(message: types.Message):
    total_count = model.get_total_candies()
    max = model.get_max_take()
    model.set_max_take(max)
    if total_count <= max:
        enemy_take = total_count
    else:
        enemy_take = (total_count - 1)%max
    total = total_count - enemy_take
    await view.remainder_bot(message, enemy_take, total)
    if model.check_win(total):
        await view.looser(message)
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(message)


async def await_player(message: types.Message):
    max_take = model.get_max_take()
    model.set_max_take(max_take)
    await view.take_max(message, max_take)


async def set_total_candies(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await view.change_max(message, count)

    
async def one_move(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_max_take(count)
    await view.count_candy(message, count)
    
async def help(message: types.Message):
    await view.help_message(message)
    