import 'package:flutter/material.dart';

class FancyButton extends StatelessWidget {
  FancyButton({this.onPressed});

  final GestureTapCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return RawMaterialButton(
      fillColor: Colors.deepOrange,
      splashColor: Colors.orange,
      child: Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 20.0,
          horizontal: 100.0,
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.drive_eta,
              color: Colors.amber,
            ),
            const SizedBox(width: 9.0),
            Text(
              'New Order',
              style: TextStyle(
                color: Colors.white,
                fontSize: 20.0,

              ),
            ),
          ],
        ),
      ),
      onPressed: onPressed,
      shape: const StadiumBorder(),
    );
  }
}
