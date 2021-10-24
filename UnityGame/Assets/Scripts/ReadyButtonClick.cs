using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ReadyButtonClick : MonoBehaviour
{
    public GameObject counterText;
    public GameObject readyButton;
    public GameObject cameraFeed;
    // Start is called before the first frame update
    void Start()
    {
      
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void readyClicked()
    {
        cameraFeed.SetActive(true);
        readyButton.SetActive(false);
        counterText.SetActive(true);
    }

    public void makeCameraFeedActive()
    {

    }

    public void disableCameraFeed()
    {

    }

    public void enableCounter()
    {

    }
}
