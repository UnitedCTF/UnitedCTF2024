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

#include <cstdlib>
#include <iostream>
#include <thread>
#include <cstring>
#include <utility>
#include <boost/asio/ts/buffer.hpp>
#include <boost/asio/ts/internet.hpp>

using boost::asio::ip::tcp;

const int max_length = 10;

void session(tcp::socket sock)
{
  try
  {
    boost::asio::write(sock, boost::asio::buffer("Bienvenue à UnitedSlots Admin. Welcome to UnitedSlots Admin.\n\nEntrer le mot de passe / Enter the password:\n"));
    char override[2] = "n"; // UnitedSlots: change this when doing development
    char password[max_length];
    boost::system::error_code error;
    size_t length = 0;
    bool shouldStopReading = false;
    for (;;)
    {
      length += sock.read_some(boost::asio::buffer(password + length, 100), error);

      if (error == boost::asio::stream_errc::eof)
        break; // Connection closed cleanly by peer.
      else if (error)
        throw boost::system::system_error(error); // Some other error.
      
      for(int i=0; i<length; i++){
        if(password[i]=='\n') {
          shouldStopReading = true;
        }
      }
      if(shouldStopReading){
        break;
      }
    }

    char* envPassword = getenv("PASSWORD1");
    if(envPassword == nullptr){
        exit(1);
    }

    if(strcmp(password, envPassword)==0 || override[0]=='y'){
      boost::asio::write(sock, boost::asio::buffer("Accès autorisé! Authorized access!"));
      char* flag = getenv("FLAG1");
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
