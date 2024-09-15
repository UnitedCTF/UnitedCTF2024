//
// blocking_tcp_echo_server.cpp (main.cpp)
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
// Copyright (c) 2003-2024 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//
// Modified Sept 8th, 2024 by Ch0ufleur : https://ch0ufleur.dev
// Modified Sept 15th, 2024 by Linkster78 : https://github.com/Linkster78

#include <cstdlib>
#include <iostream>
#include <thread>
#include <cstring>
#include <utility>
#include <boost/asio/ts/buffer.hpp>
#include <boost/asio/ts/internet.hpp>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using boost::asio::ip::tcp;

const int max_length = 10;

// modified from example to support ascii https://en.cppreference.com/w/c/string/multibyte/mblen
size_t strlen_mb(const char* ptr)
{
  size_t result = 0;
  const char* end = ptr + strlen(ptr);
  mblen(NULL, 0);
  while(ptr < end) {
      int next = mblen(ptr, end - ptr);
      ptr += std::abs(next);
      ++result;
  }
  return result;
}

void session(tcp::socket sock)
{
  try
  {
    char override[16] = {0};
    char password[max_length] = {0};
    override[0] = 'n'; // UnitedSlots: change this when doing development

    boost::asio::write(sock, boost::asio::buffer("Bienvenue à UnitedSlots Admin. Welcome to UnitedSlots Admin.\n\nEntrer le mot de passe / Enter the password:\n"));
    boost::system::error_code error;

    char* readPtr = password;
    while(readPtr + 1 < password + max_length)
    {
      size_t length = strlen_mb(password);
      size_t read = sock.read_some(boost::asio::buffer(readPtr, std::max(0, max_length - 1 - (int)length)), error);
      readPtr += read;

      if (error == boost::asio::stream_errc::eof)
        break; // Connection closed cleanly by peer.
      else if (error)
        throw boost::system::system_error(error); // Some other error.

      for(char* ptr=password; ptr < readPtr; ++ptr){
        if(*ptr == '\n' || *ptr == '\0')
          goto doneRead;
      }
    }

doneRead:
    char* envPassword = getenv("PASSWORD2");
    if(envPassword == nullptr){
        exit(1);
    }

    if(strcmp(password, envPassword)==0 || strcmp(override, "y")==0){
      boost::asio::write(sock, boost::asio::buffer("Accès autorisé! Authorized access!\n"));
      char* flag = getenv("FLAG2");
      if(flag == nullptr){
        exit(1);
      }
      boost::asio::write(sock, boost::asio::buffer(flag, strlen(flag)));
    }
    else {
      boost::asio::write(sock, boost::asio::buffer("Bye bye!\n"));
    }
  }
  catch (std::exception& e)
  {
    std::cerr << "Exception in thread: " << e.what() << "\n";
  }
}

void server(boost::asio::io_context& io_context, unsigned short port)
{
  tcp::acceptor a(io_context, tcp::endpoint(tcp::v4(), port));
  for (;;)
  {
    tcp::socket sock(io_context);
    a.accept(sock);
    std::thread(session, std::move(sock)).detach();
  }
}

int main(int argc, char* argv[])
{
  setlocale(LC_ALL, "en_US.utf8");

  try
  {
    if (argc != 2)
    {
      std::cerr << "Usage: ./UnitedSlots <port>\n";
      return 1;
    }

    boost::asio::io_context io_context;

    server(io_context, std::atoi(argv[1]));
  }
  catch (std::exception& e)
  {
    std::cerr << "Exception: " << e.what() << "\n";
  }

  return 0;
}
