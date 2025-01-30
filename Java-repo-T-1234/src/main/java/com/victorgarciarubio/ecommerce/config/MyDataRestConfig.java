package com.victorgarciarubio.ecommerce.config;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import javax.persistence.EntityManager;
import javax.persistence.metamodel.EntityType;

import com.victorgarciarubio.ecommerce.entity.Product;
import com.victorgarciarubio.ecommerce.entity.ProductCategory;
import com.victorgarciarubio.ecommerce.entity.Country;
import com.victorgarciarubio.ecommerce.entity.State;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.rest.core.config.RepositoryRestConfiguration;
import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
import org.springframework.http.HttpMethod;
import org.springframework.web.servlet.config.annotation.CorsRegistry;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@Configuration
@Api(tags = "Data REST Configuration")
public class MyDataRestConfig implements RepositoryRestConfigurer {

    private EntityManager entityManager;

    @Autowired
    public MyDataRestConfig(EntityManager myEntityManager) {
        entityManager = myEntityManager;
    }

    @Override
    @ApiOperation(value = "Configure Repository REST", notes = "Configures the REST repository settings including CORS, HTTP methods, and entity ID exposure")
    public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config, CorsRegistry cors) {
        HttpMethod[] unsupportedActions = {
            HttpMethod.PUT, HttpMethod.POST, HttpMethod.DELETE
        };

        disableHttpMethods(Product.class, config, unsupportedActions);
        disableHttpMethods(ProductCategory.class, config, unsupportedActions);
        disableHttpMethods(Country.class, config, unsupportedActions);
        disableHttpMethods(State.class, config, unsupportedActions);

        exposeIds(config);
    }

    private void disableHttpMethods(Class<?> disabledClass, RepositoryRestConfiguration config, HttpMethod[] unsupportedActions) {
        config.getExposureConfiguration()
            .forDomainType(disabledClass)
            .withItemExposure((metdata, httpMethods) -> httpMethods.disable(unsupportedActions))
            .withCollectionExposure((metdata, httpMethods) -> httpMethods.disable(unsupportedActions));
    }

    private void exposeIds(RepositoryRestConfiguration config) {
        Set<EntityType<?>> entities = entityManager.getMetamodel().getEntities();
        List<Class<?>> entityClasses = new ArrayList<>();

        for (EntityType<?> tempEntityType : entities) {
            entityClasses.add(tempEntityType.getJavaType());
        }

        Class<?>[] domainTypes = entityClasses.toArray(new Class<?>[0]);
        config.exposeIdsFor(domainTypes);
    }
}