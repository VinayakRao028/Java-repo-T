package com.victorgarciarubio.ecommerce.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Data;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@Entity
@Table(name = "state")
@Data
@ApiModel(description = "Entity representing a state")
public class State {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    @ApiModelProperty(value = "The unique identifier of the state", example = "1")
    private int id;

    @Column(name = "name")
    @ApiModelProperty(value = "The name of the state", example = "California")
    private String name;

    @ManyToOne
    @JoinColumn(name = "country_id")
    @ApiModelProperty(value = "The country to which this state belongs")
    private Country country;
}