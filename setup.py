from setuptools import setup

setup(
  name = 'cfscrape',
  packages = ['cfscrape'],
  version = '1.9.0',
  description = 'A simple Python module to bypass Cloudflare\'s anti-bot page. See https://github.com/Anorov/cloudflare-scrape for more information.',
  author = 'Anorov',
  author_email = 'anorov.vorona@gmail.com',
  url = 'https://github.com/Anorov/cloudflare-scrape',
  keywords = ['cloudflare', 'scraping'],
  install_requires = ['PyExecJS >= 1.4.0', 'requests >= 2.0.0']
)
