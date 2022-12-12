using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Collections.Generic;
using UnityEngine.UIElements;

public class hand_detector : MonoBehaviour
{
    private JsonFile _jsonFile;
    private string _coord = "";

    static IPHostEntry host = Dns.GetHostEntry("localhost");
    // "192.168.1.71", 11111
    // static IPHostEntry host = Dns.GetHostEntry("127.0.0.1");
    static IPAddress iPAddress = host.AddressList[1];
    static IPEndPoint remoteEP = new IPEndPoint(iPAddress, 8081);
    static Socket sender = new Socket(iPAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

    byte[] bytes;
    int bytesRec;

    private static List<string> WRIST_coord = new List<string> {"", "", ""};
    private static List<string> THUMB_CMC_coord = new List<string> {"", "", ""};
    private static List<string> THUMB_MCP_coord = new List<string> {"", "", ""};
    private static List<string> THUMB_IP_coord = new List<string> {"", "", ""};
    private static List<string> THUMB_TIP_coord = new List<string> {"", "", ""};
    private static List<string> INDEX_FINGER_MCP_coord = new List<string> {"", "", ""};
    private static List<string> INDEX_FINGER_PIP_coord = new List<string> {"", "", ""};
    private static List<string> INDEX_FINGER_DIP_coord = new List<string> {"", "", ""};
    private static List<string> INDEX_FINGER_TIP_coord = new List<string> {"", "", ""};
    private static List<string> MIDDLE_FINGER_MCP_coord = new List<string> {"", "", ""};
    private static List<string> MIDDLE_FINGER_PIP_coord = new List<string> {"", "", ""};
    private static List<string> MIDDLE_FINGER_DIP_coord = new List<string> {"", "", ""};
    private static List<string> MIDDLE_FINGER_TIP_coord = new List<string> {"", "", ""};
    private static List<string> RING_FINGER_MCP_coord = new List<string> {"", "", ""};
    private static List<string> RING_FINGER_PIP_coord = new List<string> {"", "", ""};
    private static List<string> RING_FINGER_DIP_coord = new List<string> {"", "", ""};
    private static List<string> RING_FINGER_TIP_coord = new List<string> {"", "", ""};
    private static List<string> PINKY_MCP_coord = new List<string> {"", "", ""};
    private static List<string> PINKY_PIP_coord = new List<string> {"", "", ""};
    private static List<string> PINKY_DIP_coord = new List<string> {"", "", ""};
    private static List<string> PINKY_TIP_coord = new List<string> {"", "", ""};

    [SerializeField] private GameObject[] _points;

    private void Start()
    {
        StartClient();
    }


    private void Update()
    {
        newCoord();

        if (_coord != "" && _coord != "nothing") 
            handMove();
    }

    private void handMove()
    {
        _points[0].transform.position = new Vector3(-Convert.ToSingle(WRIST_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(WRIST_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(WRIST_coord[2].Replace(".", ",")));
        _points[1].transform.position = new Vector3(-Convert.ToSingle(THUMB_CMC_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(THUMB_CMC_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(THUMB_CMC_coord[2].Replace(".", ",")));
        _points[2].transform.position = new Vector3(-Convert.ToSingle(THUMB_MCP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(THUMB_MCP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(THUMB_MCP_coord[2].Replace(".", ",")));
        _points[3].transform.position = new Vector3(-Convert.ToSingle(THUMB_IP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(THUMB_IP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(THUMB_IP_coord[2].Replace(".", ",")));
        _points[4].transform.position = new Vector3(-Convert.ToSingle(THUMB_TIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(THUMB_TIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(THUMB_TIP_coord[2].Replace(".", ",")));
        _points[5].transform.position = new Vector3(-Convert.ToSingle(INDEX_FINGER_MCP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(INDEX_FINGER_MCP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(INDEX_FINGER_MCP_coord[2].Replace(".", ",")));
        _points[6].transform.position = new Vector3(-Convert.ToSingle(INDEX_FINGER_PIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(INDEX_FINGER_PIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(INDEX_FINGER_PIP_coord[2].Replace(".", ",")));
        _points[7].transform.position = new Vector3(-Convert.ToSingle(INDEX_FINGER_DIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(INDEX_FINGER_DIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(INDEX_FINGER_DIP_coord[2].Replace(".", ",")));
        _points[8].transform.position = new Vector3(-Convert.ToSingle(INDEX_FINGER_TIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(INDEX_FINGER_TIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(INDEX_FINGER_TIP_coord[2].Replace(".", ",")));
        _points[9].transform.position = new Vector3(-Convert.ToSingle(MIDDLE_FINGER_MCP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(MIDDLE_FINGER_MCP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(MIDDLE_FINGER_MCP_coord[2].Replace(".", ",")));
        _points[10].transform.position = new Vector3(-Convert.ToSingle(MIDDLE_FINGER_PIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(MIDDLE_FINGER_PIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(MIDDLE_FINGER_PIP_coord[2].Replace(".", ",")));
        _points[11].transform.position = new Vector3(-Convert.ToSingle(MIDDLE_FINGER_DIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(MIDDLE_FINGER_DIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(MIDDLE_FINGER_DIP_coord[2].Replace(".", ",")));
        _points[12].transform.position = new Vector3(-Convert.ToSingle(MIDDLE_FINGER_TIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(MIDDLE_FINGER_TIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(MIDDLE_FINGER_TIP_coord[2].Replace(".", ",")));
        _points[13].transform.position = new Vector3(-Convert.ToSingle(RING_FINGER_MCP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(RING_FINGER_MCP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(RING_FINGER_MCP_coord[2].Replace(".", ",")));
        _points[14].transform.position = new Vector3(-Convert.ToSingle(RING_FINGER_PIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(RING_FINGER_PIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(RING_FINGER_PIP_coord[2].Replace(".", ",")));
        _points[15].transform.position = new Vector3(-Convert.ToSingle(RING_FINGER_DIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(RING_FINGER_DIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(RING_FINGER_DIP_coord[2].Replace(".", ",")));
        _points[16].transform.position = new Vector3(-Convert.ToSingle(RING_FINGER_TIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(RING_FINGER_TIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(RING_FINGER_TIP_coord[2].Replace(".", ",")));
        _points[17].transform.position = new Vector3(-Convert.ToSingle(PINKY_MCP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(PINKY_MCP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(PINKY_MCP_coord[2].Replace(".", ",")));
        _points[18].transform.position = new Vector3(-Convert.ToSingle(PINKY_PIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(PINKY_PIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(PINKY_PIP_coord[2].Replace(".", ",")));
        _points[19].transform.position = new Vector3(-Convert.ToSingle(PINKY_DIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(PINKY_DIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(PINKY_DIP_coord[2].Replace(".", ",")));
        _points[20].transform.position = new Vector3(-Convert.ToSingle(PINKY_TIP_coord[0].Replace(".", ",")) + 400f, -Convert.ToSingle(PINKY_TIP_coord[1].Replace(".", ",")) + 200f, -Convert.ToSingle(PINKY_TIP_coord[2].Replace(".", ",")));
    }

    private void newCoord()
    {
        bytes = new byte[4096];
        bytesRec = sender.Receive(bytes);
        _coord = Encoding.ASCII.GetString(bytes, 0, bytesRec);

        if (_coord != "" && _coord != "nothing")
        {
            _jsonFile = JsonUtility.FromJson<JsonFile>(_coord.Replace("'", "\""));

            WRIST_coord = new List<string>(_jsonFile.WRIST.Split("_"));
            THUMB_CMC_coord = new List<string>(_jsonFile.THUMB_CMC.Split("_"));
            THUMB_MCP_coord = new List<string>(_jsonFile.THUMB_MCP.Split("_"));
            THUMB_IP_coord = new List<string>(_jsonFile.THUMB_IP.Split("_"));
            THUMB_TIP_coord = new List<string>(_jsonFile.THUMB_TIP.Split("_"));
            INDEX_FINGER_MCP_coord = new List<string>(_jsonFile.INDEX_FINGER_MCP.Split("_"));
            INDEX_FINGER_PIP_coord = new List<string>(_jsonFile.INDEX_FINGER_PIP.Split("_"));
            INDEX_FINGER_DIP_coord = new List<string>(_jsonFile.INDEX_FINGER_DIP.Split("_"));
            INDEX_FINGER_TIP_coord = new List<string>(_jsonFile.INDEX_FINGER_TIP.Split("_"));
            MIDDLE_FINGER_MCP_coord = new List<string>(_jsonFile.MIDDLE_FINGER_MCP.Split("_"));
            MIDDLE_FINGER_PIP_coord = new List<string>(_jsonFile.MIDDLE_FINGER_PIP.Split("_"));
            MIDDLE_FINGER_DIP_coord = new List<string>(_jsonFile.MIDDLE_FINGER_DIP.Split("_"));
            MIDDLE_FINGER_TIP_coord = new List<string>(_jsonFile.MIDDLE_FINGER_TIP.Split("_"));
            RING_FINGER_MCP_coord = new List<string>(_jsonFile.RING_FINGER_MCP.Split("_"));
            RING_FINGER_PIP_coord = new List<string>(_jsonFile.RING_FINGER_PIP.Split("_"));
            RING_FINGER_DIP_coord = new List<string>(_jsonFile.RING_FINGER_DIP.Split("_"));
            RING_FINGER_TIP_coord = new List<string>(_jsonFile.RING_FINGER_TIP.Split("_"));
            PINKY_MCP_coord = new List<string>(_jsonFile.PINKY_MCP.Split("_"));
            PINKY_PIP_coord = new List<string>(_jsonFile.PINKY_PIP.Split("_"));
            PINKY_DIP_coord = new List<string>(_jsonFile.PINKY_DIP.Split("_"));
            PINKY_TIP_coord = new List<string>(_jsonFile.PINKY_TIP.Split("_"));
        }
    }

    private void StartClient()
    {
        try
        {
            sender.Connect(remoteEP);
        }
        catch
        {
            sender.Shutdown(SocketShutdown.Both);
            sender.Close();
        }
    }
}

[System.Serializable]
public class JsonFile
{
    public string WRIST;
    public string THUMB_CMC;
    public string THUMB_MCP;
    public string THUMB_IP;
    public string THUMB_TIP;
    public string INDEX_FINGER_MCP;
    public string INDEX_FINGER_PIP;
    public string INDEX_FINGER_DIP;
    public string INDEX_FINGER_TIP;
    public string MIDDLE_FINGER_MCP;
    public string MIDDLE_FINGER_PIP;
    public string MIDDLE_FINGER_DIP;
    public string MIDDLE_FINGER_TIP;
    public string RING_FINGER_MCP;
    public string RING_FINGER_PIP;
    public string RING_FINGER_DIP;
    public string RING_FINGER_TIP;
    public string PINKY_MCP;
    public string PINKY_PIP;
    public string PINKY_DIP;
    public string PINKY_TIP;
}
