// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "PassportEntry.generated.h"

/**
 * 
 */
UCLASS()
class ADVENTOFCODE2020_API UPassportEntry : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

	UFUNCTION(BlueprintCallable, category = "Validation")
	static bool HairColorIsValid(FString InColor);
};
