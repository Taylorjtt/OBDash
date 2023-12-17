#ifndef SPEKTACH_H
#define SPEKTACH_H

#include <QMainWindow>

namespace Ui {
class SpekTach;
}

class SpekTach : public QMainWindow
{
    Q_OBJECT

public:
    explicit SpekTach(QWidget *parent = nullptr);
    ~SpekTach();

private:
    Ui::SpekTach *ui;
};

#endif // SPEKTACH_H
