# -*- coding: utf-8 -*-
"""
===================================
Robot Command Trigger System
===================================

Trigger stock analysis and other functions via @robot or sending commands.
Supports multiple platforms including Feishu, DingTalk, WeCom, Telegram, etc.

Module structure:
- models.py: Unified message/response model
- dispatcher.py: Command dispatcher
- commands/: Command handlers
- platforms/: Platform adapters
- handler.py: Webhook handler

Usage:
1. Configure environment variables (tokens for each platform, etc.)
2. Start WebUI service
3. Configure Webhook URLs on each platform:
   - Feishu: http://your-server/bot/feishu
   - DingTalk: http://your-server/bot/dingtalk
   - WeCom: http://your-server/bot/wecom
   - Telegram: http://your-server/bot/telegram

Supported commands:
- /analyze <stock_code>  - Analyze specified stock
- /market             - Market review
- /batch              - Batch analysis of self-selected stocks
- /help               - Show help
- /status             - System status
"""

from bot.models import BotMessage, BotResponse, ChatType, WebhookResponse
from bot.dispatcher import CommandDispatcher, get_dispatcher

__all__ = [
    'BotMessage',
    'BotResponse',
    'ChatType',
    'WebhookResponse',
    'CommandDispatcher',
    'get_dispatcher',
]