## Descripción
Can you reverse this [Windows Binary](https://jupiter.challenges.picoctf.org/static/0ef5d0d6d552cd5e0bd60c2adbddaa94/win-exec-1.exe)?

## Hints
+ Microsoft provides windows virtual machines https://developer.microsoft.com/en-us/windows/downloads/virtual-machines
+  Ollydbg may be helpful
+ Flag format: PICOCTF{XXXX}

## Solución

``` 

void FUN_00408040(void)

{
  int iVar1;
  FILE *_File;
  uint uVar2;
  undefined extraout_DL;
  undefined extraout_DL_00;
  undefined extraout_DL_01;
  undefined uVar3;
  undefined uVar4;
  void *in_stack_ffffff88;
  int local_74;
  char local_6c [100];
  uint local_8;
  
  local_8 = DAT_0047b174 ^ (uint)&stack0xfffffffc;
  thunk_FUN_004083e0((wchar_t *)s_Input_a_number_between_1_and_5_d_0047b06c);
  thunk_FUN_00408430((wchar_t *)&DAT_0047b094);
  local_74 = 1;
  for (; 9 < (int)in_stack_ffffff88; in_stack_ffffff88 = (void *)((int)in_stack_ffffff88 / 10)) {
    local_74 = local_74 + 1;
  }
  if (local_74 < 6) {
    thunk_FUN_004083e0((wchar_t *)s_Initializing..._0047b0b4);
    thunk_FUN_00407ff0(in_stack_ffffff88,local_74);
    do {
      iVar1 = __fgetchar();
      uVar4 = SUB41(in_stack_ffffff88,0);
    } while (iVar1 != 10);
    thunk_FUN_004083e0((wchar_t *)s_Enter_the_correct_key_to_get_the_0047b0c8);
    _File = (FILE *)___acrt_iob_func(0);
    _fgets(local_6c,100,_File);
    uVar2 = thunk_FUN_00407f60(local_6c);
    if ((char)uVar2 == '\0') {
      thunk_FUN_004083e0((wchar_t *)s_Incorrect_key._Try_again._0047b0f8);
      uVar3 = extraout_DL_00;
    }
    else {
      thunk_FUN_004083e0((wchar_t *)s_Correct_input._Printing_flag:_0047b114);
      thunk_FUN_00408010();
      uVar3 = extraout_DL_01;
    }
  }
  else {
    thunk_FUN_004083e0((wchar_t *)s_Number_too_big._Try_again._0047b098);
    uVar4 = SUB41(in_stack_ffffff88,0);
    uVar3 = extraout_DL;
  }
  thunk_FUN_004084bf(local_8 ^ (uint)&stack0xfffffffc,uVar3,uVar4);
  return;
}

```

código parchado 

``` 
void FUN_00408040(void)

{
  int iVar1;
  FILE *_File;
  undefined extraout_DL;
  undefined extraout_DL_00;
  undefined uVar2;
  undefined uVar3;
  void *in_stack_ffffff88;
  int local_74;
  char local_6c [100];
  uint local_8;
  
  local_8 = DAT_0047b174 ^ (uint)&stack0xfffffffc;
  thunk_FUN_004083e0((wchar_t *)s_Input_a_number_between_1_and_5_d_0047b06c);
  thunk_FUN_00408430((wchar_t *)&DAT_0047b094);
  local_74 = 1;
  for (; 9 < (int)in_stack_ffffff88; in_stack_ffffff88 = (void *)((int)in_stack_ffffff88 / 10)) {
    local_74 = local_74 + 1;
  }
  if (local_74 < 6) {
    thunk_FUN_004083e0((wchar_t *)s_Initializing..._0047b0b4);
    thunk_FUN_00407ff0(in_stack_ffffff88,local_74);
    do {
      iVar1 = __fgetchar();
      uVar3 = SUB41(in_stack_ffffff88,0);
    } while (iVar1 != 10);
    thunk_FUN_004083e0((wchar_t *)s_Enter_the_correct_key_to_get_the_0047b0c8);
    _File = (FILE *)___acrt_iob_func(0);
    _fgets(local_6c,100,_File);
    thunk_FUN_00407f60(local_6c);
    thunk_FUN_004083e0((wchar_t *)s_Correct_input._Printing_flag:_0047b114);
    thunk_FUN_00408010();
    uVar2 = extraout_DL_00;
  }
  else {
    thunk_FUN_004083e0((wchar_t *)s_Number_too_big._Try_again._0047b098);
    uVar3 = SUB41(in_stack_ffffff88,0);
    uVar2 = extraout_DL;
  }
  thunk_FUN_004084bf(local_8 ^ (uint)&stack0xfffffffc,uVar2,uVar3);
  return;
}
```

ejecucion del archivo modificado
``` bash 
C:\Users\Odalys\Desktop>modify_binary.exe                                         Input a number between 1 and 5 digits: 2                                         Initializing...                                                                   Enter the correct key to get the access codes: 1234                               Correct input. Printing flag: PICOCTF{These are the access codes to the vault: 1063340}                                 

 C:\Users\Odalys\Desktop>
```


## Flag
==PICOCTF{These are the access codes to the vault: 1063340}== 



## Notas adicionales




## Referencias
+ [wine](https://www.winehq.org/)
+ [x86 assembly](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow)