#include <iostream>
#include <string>
using namespace std;
class Human {
private:
    string name;   
    string pol;
    int age;      
public:
    Human(string n, string g, int a) {
        name = n;
        pol = g;
        age = a;
    }
    int getAge() {
        return age;
    }
    void show() {
        cout << "Имя: " << name << ", Пол: " << pol << ", Возраст: " << age << endl;
    }
};
int main() {
    setlocale(LC_ALL, "Russian");
    const int count = 3;
    Human* h[count];
    h[0] = new Human("Катя", "Ж", 25);
    h[1] = new Human("Анна", "Ж", 30);
    h[2] = new Human("Семён", "М", 17);
    int minAge, maxAge;
    cout << "минимальный возраст: ";
    cin >> minAge;
    cout << "максимальный возраст: ";
    cin >> maxAge;
    bool found = false;
    for (int i = 0; i < count; i++) {
        if (h[i]->getAge() >= minAge && h[i]->getAge() <= maxAge) {
            h[i]->show();
            found = true;
        }
    }
    if (!found) {
        cout << "Никто не подходит" << endl;
    }
    for (int i = 0; i < count; i++) {
        delete h[i];
        h[i] = nullptr;
    }
    return 0;
}
