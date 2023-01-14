from scapy.all import *
from colorama import Fore, Back, Style
import textwrap
import socket
import struct
import time
import psutil


class interceptor:
  """
  A backend class for network interceptor...
  
  """

  def __init__(self):
    self.log_path = './assets/log.txt'

  def block(self, domain):
    pass

  def bandwidth(self):

    last_received = psutil.net_io_counters().bytes_recv
    last_send = psutil.net_io_counters().bytes_sent
    last_total = last_received + last_send

    while True:
      byte_received = psutil.net_io_counters().bytes_recv
      byte_send = psutil.net_io_counters().bytes_sent
      byte_total = byte_received + byte_send

      new_received = byte_received - last_received
      new_send = byte_send - last_send

      new_total = byte_total - last_total

      mb_new_recv = new_received / 1024 / 1024
      mb_new_sent = new_send / 1024 / 1024
      mb_new_total = new_total / 1024 / 1024

      print(
        f"{mb_new_recv:.2f} MB recv, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total"
      )

  def sniff_reveal_log(self, data):
    with open(self.log_path, "a") as file:
      file.write(str(data))
      file.write("\n")
      print(Fore.RED + str(data))

  def sniff_reveal(self, data):
    print(Fore.RED + str(data))

  def sniffandlog(self):
    sniff(prn = self.sniff_reveal_log)

  def sniffonly(self):
    sniff(prn= self.sniff_reveal)

