package com.victorgarciarubio.ecommerce.entity;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

import lombok.Data;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@Entity
@Table(name = "country")
@Data
@ApiModel(description = "Entity representing a country")
public class Country {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    @ApiModelProperty(value = "The unique identifier of the country", example = "1")
    private int id;

    @Column(name = "code")
    @ApiModelProperty(value = "The country code", example = "US")
    private String code;

    @Column(name = "name")
    @ApiModelProperty(value = "The name of the country", example = "United States")
    private String name;

    @OneToMany(mappedBy = "country")
    @JsonIgnore // Ignore in response json
    @ApiModelProperty(value = "The list of states in the country")
    private List<State> states;
}