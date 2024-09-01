#include <iostream>
#include <chrono>
#include <thread>
#include <string>

void win_screen() {
    int duration = 5000;
    int interval = 300;
    int steps = duration / interval;

    std::cout << "Loading";
    
    for (int i = 0; i < steps; ++i) {
        std::cout << ".";
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::milliseconds(interval));
    }

    std::cout << " flag-d0nT5HarEy0urP@s5owRd" << std::endl;
}

bool valid_password(const std::string& str1, const std::string& str2) {
    auto start = std::chrono::high_resolution_clock::now();
    bool result = (str1 == str2);

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> elapsed = end - start;

    if (elapsed.count() < 500)
        std::this_thread::sleep_for(std::chrono::milliseconds(500) - elapsed);

    return result;
}

int main() {
    std::string password;
    std::cout << "[sudo] password for marc: ";
    std::cin >> password;

    if (valid_password(password, "metallica")) {
        win_screen();
    } else {
        std::cout << "Sorry, try again." << std::endl;
    }
    

    return 0;
}