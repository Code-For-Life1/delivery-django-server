import 'package:delivery_app/driver_add.dart';
import 'package:delivery_app/driver_signup.dart';
import 'package:flutter/material.dart';

class MerchantDrivers extends StatefulWidget {
  @override
  _MerchantDriversState createState() => _MerchantDriversState();
}

class _MerchantDriversState extends State<MerchantDrivers> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
        title: Text('Drivers'),
        centerTitle: true,
        backgroundColor: Colors.orange[800],
        actions: [
         IconButton(icon: Icon(Icons.add), onPressed: (){
           Navigator.push(context, MaterialPageRoute(
               builder: (context) => DriverAdd()
           ));
         })
        ],
      ),
      body: ListView.builder(
        itemCount: 20,
        itemBuilder: (context,index){
          return Card(
            color: Colors.amber,
            child: Column(
              children: [
                Text('Driver${index+1}'),
                Text('Name: Mahmoud'),
                Text('Hello3')
              ],
            ),
          );
        }
      )
    );
  }
}
