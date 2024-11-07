import 'dart:math';
import "dart:io";

void main() {
  stdout.write('Enter your username.');
  String username = stdin.readLineSync()!;
  String password = randomPassword();

  print('username: ${username} password: ${password}');
  user user1 = user(username, password);

  print(user1.getPassword());

  user1.changePassword();

  user1.login();
}

String randomPassword() {
  var random1 = Random().nextInt(31);
  var random2 = Random().nextInt(31);
  var random3 = Random().nextInt(31);
  //final string1 = String.fromCharCodes([random1]);
  //final string2 = String.fromCharCodes([random2]);
  //final string3 = String.fromCharCodes([random3]);
  String output = '${random1}${random2}${random3}';
  return output;
}

class user {
  String username;
  String _password;

  user(this.username, this._password);

  String getPassword() {
    return _password;
  }

  void changePassword() {
    stdout.write('Enter current password.');
    String passwordCheck = stdin.readLineSync()!;
    if (passwordCheck == _password) {
      stdout.write('Enter new password.');
      var newPassword = stdin.readLineSync()!;
      _password = newPassword;
      print('Password changed.');
    }
    else {
      print('Incorrect password.');
    }
  }

  bool login() {
    stdout.write('Enter your password.');
    String accountCheck = stdin.readLineSync()!;
    if (accountCheck == _password) {
      print('Login successful.');
      return true;
    }
    else {
      print('Password incorrect.');
      return false;
    }
  }

}