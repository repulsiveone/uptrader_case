from django.db import models
from django.urls import reverse


class MenuModel(models.Model):
	name = models.CharField("название", max_length=100)
	url = models.CharField("url", max_length=255)
	named_url = models.CharField("именованный url", max_length=100)
	parent = models.ForeignKey(
		"self",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name="children",
	)
	menu_name = models.CharField("название меню", max_length=60)

	def get_url(self):
		"""Возвращает: именованный URL (через reverse), прямой URL или корневой URL"""
		if self.named_url:
			return reverse(self.named_url)
		return self.url or '/'