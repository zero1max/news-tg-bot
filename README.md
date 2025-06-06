# Telegram News Bot

A Telegram bot that delivers news from different categories including World News, Sports, Science, and Business.

## Features

- 📰 News delivery in multiple categories:
  - 🌍 World News
  - 🏅 Sports
  - 🧬 Science
  - 💼 Business
- Image support for news articles
- User-friendly interface with category selection
- Admin panel for news management
- MongoDB database integration

## Technical Stack

- Python 3.x
- aiogram 3.20.0 (Telegram Bot Framework)
- MongoDB (Database)
- Motor (Async MongoDB driver)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd news-tg-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```
BOT_TOKEN=your_telegram_bot_token
MONGODB_URI=your_mongodb_connection_string
```

## Usage

1. Start the bot:
```bash
python main.py
```

2. Open Telegram and start a chat with your bot
3. Use the `/start` command to begin
4. Select news categories from the provided keyboard

## Project Structure

```
news-tg-bot/
├── handlers/           # Bot command handlers
│   ├── admin.py       # Admin panel handlers
│   └── user.py        # User interaction handlers
├── keyboards/         # Telegram keyboard layouts
├── middlewares/       # Bot middlewares
├── database/         # Database models and operations
├── main.py           # Bot entry point
├── loader.py         # Bot initialization
└── requirements.txt  # Project dependencies
```

## License

This project is licensed under the terms of the license included in the repository.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
