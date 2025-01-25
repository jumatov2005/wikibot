
try:
    from .local_settings import TELEGRAM_TOKEN
except ImportError as e:
    raise ImportError(
        "local_settings.py faylida TELEGRAM_TOKEN tushurilgan yoki lokal fayl noto'g'ri. "
        "Iltimos, local_settings.py faylini tekshiring."
    )
