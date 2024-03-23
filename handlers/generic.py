from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from modules.text import Text
from modules.bot_commands import send_msg

router = Router()

async def start_func(msg: types.Message):
    await send_msg(
        msg.chat.id, 
        Text.start_text
    )

    # from pprint import PrettyPrinter
    # pp = PrettyPrinter(indent=4)
    # pp.pprint(msg.__dict__)

async def register_generic_handlers():
    router.message.register(start_func, CommandStart())