import asyncio
from agents.telegram_agent import application, get_latest_telegram_message, send_telegram_reply
from llm.gpt_responder import get_ai_reply

seen_message = ""

async def handle_messages():
    global seen_message

    while True:
        msg = get_latest_telegram_message()
        if msg and msg["text"] != seen_message:
            seen_message = msg["text"]
            user_id = msg["sender"]

            print(f"\n New message: {seen_message}")
            prompt = f"Reply politely to: {seen_message}"
            ai_reply = get_ai_reply(prompt)

            print(f"🤖 AI reply: {ai_reply.strip()}")
            
            await send_telegram_reply(user_id, ai_reply.strip())


        await asyncio.sleep(2)

async def main():
    print(" Starting Telegram bot...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    print(" ChatBridge AI: Running...\n")
    
    await handle_messages()

if __name__ == "__main__":
    asyncio.run(main())
