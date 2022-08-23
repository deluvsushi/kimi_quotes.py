from requests import get


class KimiQuotes:
	def __init__(self):
		self.api = "https://kimiquotes.herokuapp.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}


	def get_all_quotes(self):
		return get(
			f"{self.api}/quotes",
			headers=self.headers).json()

	def get_all_quotes_by_year(self, year: int):
		return get(
			f"{self.api}/quotes/{year}",
			headers=self.headers).json()

	def get_all_unstamped_quotes(self):
		return get(
			f"{self.api}/quotes/unstamped",
			headers=self.headers).json()

	def quote_by_id(self, quote_id: int):
		return get(
			f"{self.api}/quote/{quote_id}",
			headers=self.headers).json()

	def get_random_quote(self):
		return get(
			f"{self.api}/quote",
			headers=self.headers).json()
