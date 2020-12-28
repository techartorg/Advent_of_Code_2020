// Fill out your copyright notice in the Description page of Project Settings.

#include "PassportEntry.h"

bool UPassportEntry::HairColorIsValid(FString InColor)
{
	FColor outColor = FColor::FromHex(InColor);
	if (outColor == FColor(ForceInitToZero))
	{
		return false;
	}

	return true;
}