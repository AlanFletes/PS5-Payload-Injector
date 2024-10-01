# PS5-Payload-Injector
A small GUI for injecting payloads to the ps5-jar-loader by hammer-83


![Logo](https://imgur.com/cyGEMEo.png)


## Gettin' them code

You can download the pre-built binary from the releases section, run the script directly from the py file or build the exe using the spec file, it comes in all flavors.

## Clonning the repo

Clone the project

```bash
  git clone https://github.com/StatikkRaccoon/PS5-Payload-Injector.git
```

Go to the project directory

```bash
  cd PS5-Payload-Injector
```
## Running from py file

Just run the py file like any other python script.

Run

```bash
  python PS5PayloadInjector.py
```

## Creating exe

To create the exe, the repo comes with the pre-configured spec file, you can edit it to your liking. It uses UPX, so if you don't have it, remove all related settings from the spec before build.

Install pyinstaller

```bash
  pip install pyinstaller
```
or

```bash
  python -m pip install pyinstaller
```

Build

```bash
  pyinstaller PS5PayloadInjector.spec
```
This will create a "dist" folder where the exe will be available.

## Usage

When you open/launch the srcipt, a "payloads" folder will be created along with the exe/py file, there, you can add all the payloads you plan to use frecuently and those will be displayed in the dropdown menu. You can also use the "Select Manually" option to use a select window and look for your jar anywhere on your PC.

You can write your IP in the PS5 IP textbox, or, if you are as lazy as me, click on the "Scan Network" button and the thing will do it for you in a few seconds. Make sure your PS5 is listening for connections, otherwise, the injector won't be able to find it.

Once you have your IP in the box and the payload selected, just click the "Send Payload" button and, if everything went right, the payload will send and execute on your PS5 and you will recive a message on the injector of successfully injected.

