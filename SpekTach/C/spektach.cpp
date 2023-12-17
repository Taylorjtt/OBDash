#include "spektach.h"
#include "ui_spektach.h"

SpekTach::SpekTach(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::SpekTach)
{
    ui->setupUi(this);
}

SpekTach::~SpekTach()
{
    delete ui;
}
