// To parse this JSON data, do
//
//     final merchantModel = merchantModelFromJson(jsonString);

import 'dart:convert';

MerchantModel merchantModelFromJson(String str) => MerchantModel.fromJson(json.decode(str));

String merchantModelToJson(MerchantModel data) => json.encode(data.toJson());

class MerchantModel {
  MerchantModel({
    this.username,
    this.password,
    this.firstName,
    this.lastName,
    this.phoneNumber,
  });

  String username;
  String password;
  String firstName;
  String lastName;
  String phoneNumber;

  factory MerchantModel.fromJson(Map<String, dynamic> json) => MerchantModel(
    username: json["username"],
    password: json["password"],
    firstName: json["first_name"],
    lastName: json["last_name"],
    phoneNumber: json["phone_number"],
  );

  Map<String, dynamic> toJson() => {
    "username": username,
    "password": password,
    "first_name": firstName,
    "last_name": lastName,
    "phone_number": phoneNumber,
  };
}