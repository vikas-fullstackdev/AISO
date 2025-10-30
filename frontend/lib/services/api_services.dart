import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // For Flutter Web local testing
  static const String baseUrl = "http://127.0.0.1:8000";

  static Future<Map<String, dynamic>> registerUser(String email, String password) async {
    final uri = Uri.parse("$baseUrl/register");
    final response = await http.post(
      uri,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"email": email, "password": password}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      // FastAPI returns {"detail": "..."} on errors
      try {
        final body = jsonDecode(response.body);
        return {"status": "error", "message": body["detail"] ?? response.body};
      } catch (e) {
        return {"status": "error", "message": response.body};
      }
    }
  }

  static Future<Map<String, dynamic>> loginUser(String email, String password) async {
    final uri = Uri.parse("$baseUrl/login");
    final response = await http.post(
      uri,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"email": email, "password": password}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      try {
        final body = jsonDecode(response.body);
        return {"status": "error", "message": body["detail"] ?? response.body};
      } catch (e) {
        return {"status": "error", "message": response.body};
      }
    }
  }
}
