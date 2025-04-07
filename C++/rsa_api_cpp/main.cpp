#include "rsa_cpp.h"
#include <stdio.h>

int main(int argc, char* argv[])
{
	//Uncomment the example you'd like to run.
	//spectrum_example();
	//block_iq_example();
	//dpx_example();
	char* ptr;
	double v1;
	double v2;
	double v3;
	printf(argv[1]);
	printf("\r\n");
	printf(argv[2]);
	printf("\r\n");
	printf(argv[3]);
	printf("\r\n");
	printf("debug");
	printf("\r\n");
	v1 = strtod(argv[1], &ptr);
	v2 = strtod(argv[2], &ptr);
	v3 = strtod(argv[3], &ptr);

	TRIG_SetTriggerSource(TriggerSourceIFPowerLevel);
	TRIG_SetTriggerTransition(TriggerTransitionLH);
	TRIG_SetTriggerMode(triggered);

	double v_th = 1;
	double trig_voltage = 0.2;
	do
	{
		ReturnStatus b = TRIG_GetIFPowerTriggerLevel(&trig_voltage);
		printf("%d\n", b);
		printf("%f\n", trig_voltage);
		
		ReturnStatus a = TRIG_ForceTrigger();
		//printf("%d\n", a);
		Sleep(100);
	} while (1==1);

	iq_stream_example(v1, v2, v3);
	//if_stream_example();
	//if_playback();

}
